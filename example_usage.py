from client import AutonomousRobotPolicyEvaluatorClient

def main():
    client = AutonomousRobotPolicyEvaluatorClient()
    logs = [
        {"step": 1, "action": "Pick object", "status": "SUCCESS"},
        {"step": 2, "action": "Rotate 90deg", "status": "SUCCESS"},
        {"step": 3, "action": "Place object", "status": "FAIL", "error": "Grip slip"}
    ]
    res = client.evaluate_policy(logs, {"target": "place_object"})
    print(res["eval_result"])
    print(f"Failed Steps: {len(res['failed_steps'])}")

if __name__ == "__main__":
    main()
