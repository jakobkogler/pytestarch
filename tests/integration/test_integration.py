from __future__ import annotations

import pytest
from integration.interesting_rules_for_tests import (
    partial_name_match_test_cases,
    single_rule_subject_multiple_rule_objects_error_message_test_cases,
    single_rule_subject_single_rule_object_error_message_test_cases,
)

from pytestarch import EvaluableArchitecture
from pytestarch.query_language.base_language import RuleApplier


@pytest.mark.parametrize(
    "rule, expected_error_message",
    single_rule_subject_single_rule_object_error_message_test_cases,
)
def test_rule_violated_raises_proper_error_message(
    rule: RuleApplier,
    expected_error_message: str,
    graph_based_on_string_module_names: EvaluableArchitecture,
) -> None:
    with pytest.raises(AssertionError, match=expected_error_message):
        rule.assert_applies(graph_based_on_string_module_names)


@pytest.mark.parametrize(
    "rule, expected_error_message",
    single_rule_subject_multiple_rule_objects_error_message_test_cases,
)
def test_rule_violated_with_multiple_rule_objects_raises_proper_error_message(
    rule: RuleApplier,
    expected_error_message: str,
    graph_based_on_string_module_names: EvaluableArchitecture,
) -> None:
    with pytest.raises(AssertionError, match=expected_error_message):
        rule.assert_applies(graph_based_on_string_module_names)


@pytest.mark.parametrize("rule, violation", partial_name_match_test_cases)
def test_rule_violation_correctly_detected_for_partial_name_matches(
    rule: RuleApplier,
    violation: bool,
    graph_based_on_string_module_names: EvaluableArchitecture,
) -> None:
    if violation:
        with pytest.raises(AssertionError):
            rule.assert_applies(graph_based_on_string_module_names)
    else:
        rule.assert_applies(graph_based_on_string_module_names)
        # no exception
