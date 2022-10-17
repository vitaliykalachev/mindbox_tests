from collections import defaultdict
from labels import get_label
from typing import List, Tuple


def get_destributions_from_zero(n_customers: int):
    return get_destributions(0, n_customers)


def get_destributions(n_first_id: int, n_customers: int) -> List[Tuple]:
    assert n_first_id >= 0, f"Satring number expected positive numbers"
    assert n_customers > 0, f"Amount of customers expected positive numbers"

    result = defaultdict(int)
    for num in range(n_first_id, n_customers + n_first_id):
        result[str(get_label(num))] += 1
    return sorted(result.items(), key=lambda item: item[1], reverse=True)


