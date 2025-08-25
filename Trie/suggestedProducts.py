from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        answer = []

        for i in range(1, len(searchWord) + 1):
            products = [p for p in products if p.startswith(searchWord[:i])]
            answer.append(products[:3])
        return answer