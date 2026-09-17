class DeliverySimulator:
    def __init__(self):
        self.total_episodes = 0
        self.cumulative_reward = 0
        
    def start_episode(self):
        print("--- Starting New Delivery Episode ---")
        agent_state = {'location': 'Restaurant', 'orders_delivered': 0, 'total_reward': 0}
        
        # Hardcoded sequence of 5 actions for the simulation
        actions = [
            {'name': 'pick_up_order', 'reward': 2, 'new_location': 'Restaurant'},
            {'name': 'navigate_traffic', 'reward': -1, 'new_location': 'City Center'},
            {'name': 'deliver_order', 'reward': 10, 'new_location': 'Customer A'},
            {'name': 'wait_for_next', 'reward': -1, 'new_location': 'Customer A'},
            {'name': 'return_to_hub', 'reward': 0, 'new_location': 'Hub'}
        ]
        
        print(f"Initial State: {agent_state}")
        
        for step, act in enumerate(actions):
            # Update state
            agent_state['location'] = act['new_location']
            agent_state['total_reward'] += act['reward']
            if act['name'] == 'deliver_order':
                agent_state['orders_delivered'] += 1
                
            print(f"Step {step+1} | Action: {act['name']} | Reward: {act['reward']} | New State: {agent_state}")
            
        print("--- Episode Summary ---")
        print(f"Actions Taken: {[a['name'] for a in actions]}")
        print(f"Total Episode Reward: {agent_state['total_reward']}")
        
        self.total_episodes += 1
        self.cumulative_reward += agent_state['total_reward']
        print("Episode finished and stats saved.")

    def view_stats(self):
        print("--- Agent Cumulative Statistics ---")
        print(f"Total Episodes Run: {self.total_episodes}")
        print(f"Total Reward Earned: {self.cumulative_reward}")
        if self.total_episodes > 0:
            print(f"Average Reward per Episode: {self.cumulative_reward / self.total_episodes:.2f}")
        else:
            print("Average Reward per Episode: 0")

    def run(self):
        while True:
            print("=== Food Delivery RL Simulator ===")
            print("1. Start New Delivery Episode")
            print("2. View Agent Stats")
            print("3. Exit")
            
            choice = input("Select an option: ")
            if choice == '1':
                self.start_episode()
            elif choice == '2':
                self.view_stats()
            elif choice == '3':
                print("Exiting simulator...")
                break
            else:
                print("Invalid choice, please select 1, 2, or 3.")

if __name__ == "__main__":
    app = DeliverySimulator()
    app.run()
