from policy import Policy

class Policy2210xxx(Policy):
    def __init__(self, policy_id=1):
        assert policy_id in [1, 2], "Policy ID must be 1 or 2"

        # Student code here
        if policy_id == 1:
            self.policy = self._algorithm_one_
        elif policy_id == 2:
            self.policy = self._algorithm_two_

    def get_action(self, observation, info):
        return self.policy(observation, info)

    def algorithm_one_(self, observation, info):
        list_prods = list(observation["products"])
        
        list_prods.sort(key=lambda prod: prod["size"][0] * prod["size"][1], reverse=True)

        for prod in list_prods:
            if prod["quantity"] > 0:
                prod_size = prod["size"]

                for i, stock in enumerate(observation["stocks"]):
                    stock_w, stock_h = self._get_stock_size_(stock)
                    prod_w, prod_h = prod_size

                    if stock_w < prod_w or stock_h < prod_h:
                        continue

                    for a in range(stock_w - prod_w + 1):
                        for b in range(stock_h - prod_h + 1):
                            if self._can_place_(stock, (a, b), prod_size):
                                return {"stock_idx": i, "size": prod_size, "position": (a, b)}

        return {"stock_idx": -1, "size": [0, 0], "position": (0, 0)}

    def algorithm_two_(self, observation, info):
        # Student code here
        return None
