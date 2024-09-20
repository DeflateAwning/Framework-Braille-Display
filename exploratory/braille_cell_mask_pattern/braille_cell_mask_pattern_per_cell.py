"""Small script to figure out the optimal size and pattern for a braille cell mask.

Consider a braille cell (with 6 dots). There are 64 possible patterns for the cell (2^64).
Now, consider making a popsicle stick that you can slide back and forth over that cell to mask
out the dots. What is the optimal size for the mask? That is, what is the shortest mask that can
cover all 64 patterns?

The naive solution is to make all 64 patterns, each with 2x3 dots. At 2.5mm per dot,
this would be 480mm long (2.5mm * 3 dots * 64 patterns). However, I hypothesize that we can do
better by exploiting overlaps between the patterns.

Architecture:
-------------
    * Each braille cell row has 2 dots, which can be in 2^2 = 4 patterns.
    * Each braille cell has 3 rows.
    * A braille cell will be represented as a list of 3 numbers, where each number is a 2-bit integer (0, 1, 2, or 3).

Conclusion:
-----------
    * The optimal mask is 66 rows long.
    * The mask is a de Bruijn sequence of base 4 and length 3, with the first 2 rows repeated at the end.
    * The mask is not cyclic, which is why it is not a perfect de Bruijn sequence.
    * 🟢🟢 66 rows * 2.5mm per row = 165mm long. 🟢🟢 Pattern at bottom of file.

"""

import itertools
import random


def make_naive_mask() -> list[bool]:
    """Make a naive mask that covers all 64 patterns with 3 rows each (thus 192 rows)."""
    mask: list[int] = []
    for i in range(64):
        row_0 = i & 0b11
        row_1 = (i >> 2) & 0b11
        row_2 = (i >> 4) & 0b11
        mask.extend([row_0, row_1, row_2])

    assert len(mask) == 192
    assert all(isinstance(row, int) for row in mask)
    assert all(row in [0, 1, 2, 3] for row in mask)

    return mask


def is_complete_mask(mask: list[bool]) -> bool:
    """Check if a mask covers all 8 patterns."""
    assert isinstance(mask, list), f"Mask must be a list, not {type(mask)}."
    assert all(
        row in [0, 1, 2, 3] for row in mask
    ), "Mask must be a list of 2-bit numbers."

    for i in range(64):
        pattern = [
            i & 0b11,
            (i >> 2) & 0b11,
            (i >> 4) & 0b11,
        ]

        # If `pattern` is not a sub-list of `mask`, then `mask` is not complete.
        found_pattern = False
        for start_idx in range(0, len(mask)):
            cell_repr = mask[start_idx : start_idx + 3]
            if len(cell_repr) < 3:
                continue

            if cell_repr == pattern:
                found_pattern = True
                break

        if not found_pattern:
            return False

    # Only return True after checking (and finding) all patterns.
    return True


def count_transitions_in_mask(mask: list[bool]) -> int:
    """Count the number of transitions in a mask."""
    raise NotImplementedError(
        "This function is not yet implemented for this type of experiment."
    )
    transitions = 0

    for i in range(len(mask) - 1):
        if mask[i] != mask[i + 1]:
            transitions += 1

    return transitions


def test_every_mask(mask_length: int) -> list[list[int]]:
    """Test every mask of a given length.

    Returns:
        A list of the complete masks found.
    """
    complete_masks = []

    for cell_repr_tuple in itertools.product([0, 1, 2, 3], repeat=mask_length):
        cell_repr = list(cell_repr_tuple)

        if is_complete_mask(cell_repr):
            # transition_count = count_transitions_in_mask(cell_repr)
            transition_count = None
            print(
                f"Found complete mask ({cell_repr=}, {mask_length=}, {transition_count=}): {cell_repr}"
            )
            complete_masks.append(cell_repr)

    return complete_masks


def test_a_random_mask(mask_length: int) -> list[int] | None:
    """Test a random mask of a given length.

    Returns:
        The mask if it is complete, otherwise None.
    """

    cell_repr = [random.randint(0, 3) for _ in range(mask_length)]

    if is_complete_mask(cell_repr):
        return cell_repr

    return None


def validate_naive_mask() -> None:
    naive_mask = make_naive_mask()
    print(f"Naive mask: {naive_mask}")
    assert is_complete_mask(
        naive_mask
    ), "Naive mask is not complete. Error in implementation."
    print("Naive mask is complete.")
    print("=" * 80)


def validate_every_mask() -> None:
    for mask_length in range(3, 193):  # 192 is the maximum length
        mask_list = test_every_mask(mask_length)
        complete_mask_count = len(mask_list)
        print(f"{complete_mask_count=}, {mask_length=}")
        if complete_mask_count > 0:
            break

    print("=" * 80)


def validate_random_masks() -> None:
    tried_masks_count = 0
    success_masks_by_length: dict[int : list[int]] = {}  # mask_length -> mask
    shortest_mask_length = 200
    while 1:
        mask_length = random.randint(10, shortest_mask_length + 1)
        mask = test_a_random_mask(mask_length)
        tried_masks_count += 1
        if mask:
            success_masks_by_length[mask_length] = success_masks_by_length.get(
                mask_length, []
            ) + [mask]

            if mask_length <= shortest_mask_length:
                if mask_length < shortest_mask_length:
                    print(f"🟢🟢 New shortest length: {mask_length}")
                    shortest_mask_length = mask_length

                print(
                    f"Shortest mask length: {shortest_mask_length} (has {len(success_masks_by_length[mask_length])} masks)."
                )
                print(f"New short mask (len={mask_length}): {mask}")

        if tried_masks_count % 100_000 == 0:
            print(f"Tried {tried_masks_count:,} masks.")

    print("=" * 80)


def de_bruijn(k, n):
    """Generate a de Bruijn sequence for alphabet size k and subsequences of length n."""
    a = [0] * k * n
    sequence = []

    def db(t, p):
        if t > n:
            if n % p == 0:
                for j in range(1, p + 1):
                    sequence.append(a[j])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)

    db(1, 1)
    return sequence


def main() -> None:
    # Generate the de Bruijn sequence for base 4 and length 3.
    # This fails because de Bruijn sequences are cyclic.
    mask_test_1 = de_bruijn(4, 3)
    print(
        f"de_bruijn(4, 3) = mask_test_1: len={len(mask_test_1)}, is_complete={is_complete_mask(mask_test_1)}, {mask_test_1=}"
    )

    # Generate a non-cyclic universal sequence for base 4 and length 3.
    mask_test_2 = de_bruijn(4, 3)
    mask_test_2 = mask_test_2 + mask_test_2[:2]
    print(
        f"de_bruijn(4, 3)+first_2 = mask_test_2: len={len(mask_test_2)}, is_complete={is_complete_mask(mask_test_2)}, {mask_test_2=}"
    )

    validate_naive_mask()
    # validate_every_mask()  # Takes too long
    validate_random_masks()


# New short mask (len=109):
# [1, 2, 1, 2, 1, 1, 0, 1, 2, 2, 3, 1, 1, 0, 2, 0, 0, 2, 1, 3, 1, 2, 0, 0, 1, 3, 0, 1, 1, 1, 2, 2, 0, 3, 0, 1, 0, 0, 3, 3, 3, 0, 2, 3, 2, 0, 1, 1, 1, 3, 2, 3, 1, 2, 2, 1, 3, 3, 2, 2, 1, 2, 3, 3, 1, 1, 3, 0, 3, 2, 1, 0, 3, 2, 2, 2, 3, 2, 2, 1, 3, 1, 0, 2, 0, 2, 2, 1, 1, 2, 2, 2, 3, 0, 0, 0, 0, 3, 1, 3, 0, 0, 1, 1, 2, 3, 2, 3, 1]

# 🟢🟢 Optimal solution: 🟢🟢
# de_bruijn(4, 3)+first_2 = mask_test_2: len=66, is_complete=True
# [0, 0, 0, 1, 0, 0, 2, 0, 0, 3, 0, 1, 1, 0, 1, 2, 0, 1, 3, 0, 2, 1, 0, 2, 2, 0, 2, 3, 0, 3, 1, 0, 3, 2, 0, 3, 3, 1, 1, 1, 2, 1, 1, 3, 1, 2, 2, 1, 2, 3, 1, 3, 2, 1, 3, 3, 2, 2, 2, 3, 2, 3, 3, 3, 0, 0]

if __name__ == "__main__":
    main()
