import pytest
from engagement_engine import EngagementEngine


def test_init_default_values():
    engine = EngagementEngine("user1")
    assert engine.user_handle == "user1"
    assert engine.score == 0.0
    assert engine.verified is False


def test_init_verified_true():
    engine = EngagementEngine("creator", verified=True)
    assert engine.verified is True


def test_process_like():
    engine = EngagementEngine("user1")
    result = engine.process_interaction("like")
    assert result is True
    assert engine.score == 1


def test_process_comment_multiple():
    engine = EngagementEngine("user1")
    result = engine.process_interaction("comment", 3)
    assert result is True
    assert engine.score == 15


def test_process_share_verified():
    engine = EngagementEngine("creator", verified=True)
    result = engine.process_interaction("share", 2)
    assert result is True
    assert engine.score == 30.0


def test_process_invalid_interaction():
    engine = EngagementEngine("user1")
    result = engine.process_interaction("follow", 2)
    assert result is False
    assert engine.score == 0.0


def test_process_negative_count_raises_error():
    engine = EngagementEngine("user1")
    with pytest.raises(ValueError, match="Negative count"):
        engine.process_interaction("like", -1)


def test_get_tier_newbie():
    engine = EngagementEngine("user1")
    engine.score = 99
    assert engine.get_tier() == "Newbie"


def test_get_tier_influencer_at_100():
    engine = EngagementEngine("user1")
    engine.score = 100
    assert engine.get_tier() == "Influencer"


def test_get_tier_influencer_upper_bound():
    engine = EngagementEngine("user1")
    engine.score = 1000
    assert engine.get_tier() == "Influencer"


def test_get_tier_icon():
    engine = EngagementEngine("user1")
    engine.score = 1001
    assert engine.get_tier() == "Icon"


def test_apply_penalty_regular_case():
    engine = EngagementEngine("user1")
    engine.score = 100
    engine.apply_penalty(2)
    assert engine.score == 60


def test_apply_penalty_cannot_go_below_zero():
    engine = EngagementEngine("user1")
    engine.score = 50
    engine.apply_penalty(10)
    assert engine.score == 0


def test_apply_penalty_removes_verified_if_reports_above_10():
    engine = EngagementEngine("creator", verified=True)
    engine.score = 100
    engine.apply_penalty(11)
    assert engine.verified is False
    assert engine.score == 0


def test_apply_penalty_does_not_remove_verified_if_reports_equal_10():
    engine = EngagementEngine("creator", verified=True)
    engine.score = 100
    engine.apply_penalty(10)
    assert engine.verified is True
    assert engine.score == 0