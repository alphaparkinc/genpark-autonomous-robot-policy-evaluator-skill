class AutonomousRobotPolicyEvaluatorClient:
    def evaluate_policy(self, trajectory_logs: list, success_criteria: dict) -> dict:
        total = len(trajectory_logs)
        passed = sum(1 for log in trajectory_logs if log.get("status") == "SUCCESS")
        rate = round(passed / max(total, 1) * 100, 1)
        failed = [log for log in trajectory_logs if log.get("status") != "SUCCESS"]
        return {
            "success_rate": rate,
            "failed_steps": failed,
            "eval_result": f"Policy eval complete: {passed}/{total} steps succeeded ({rate}%)."
        }
