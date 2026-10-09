from evals.benchmark import POSITIONS, benchmark_profiles


def test_benchmark_has_sixty_labeled_cases():
    cases = benchmark_profiles()
    position_ids = {position.position_id for position in POSITIONS}

    assert len(cases) == 60
    assert len({case["case_id"] for case in cases}) == 60
    assert all(case["relevant_position_ids"] for case in cases)
    assert all(set(case["relevant_position_ids"]) <= position_ids for case in cases)
