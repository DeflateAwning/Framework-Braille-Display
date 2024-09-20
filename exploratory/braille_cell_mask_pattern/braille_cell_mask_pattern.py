"""Small script to figure out the optimal size and pattern for a braille cell mask.

Consider a column of a braille cell (with 3 dots). There are 8 possible patterns for the column (2^3).
Now, consider making a popsicle stick that you can slide back and forth over that column to mask
out the dots. What is the optimal size for the mask? That is, what is the smallest mask that can
cover all 8 patterns?

The naive solution is to make all 8 patterns, each with 3 dots (24 dots total). At 2.5mm per dot,
this would be 60mm long. However, I hypothesize that we can do better by exploiting overlaps
between the patterns.

Update: Mask Length 10 is the smallest mask that can cover all 8 patterns. There are 16 such masks.
Thus, at 2.5mm per dot, the smallest mask is about 25mm long.
"""


def int_to_bool_array(n: int, bit_length: int | None = None):
    # Convert the integer to a binary string and strip the '0b' prefix
    binary_str = bin(n)[2:]

    # If bit_length is specified, pad the binary string with leading zeros
    if bit_length:
        binary_str = binary_str.zfill(bit_length)

    # Convert the binary string to a list of boolean values
    bool_array = [bit == "1" for bit in binary_str]

    return bool_array


def make_naive_mask() -> list[bool]:
    """Make a naive mask that covers all 8 patterns with 24 dots total."""
    mask: list[bool] = []
    for i in range(8):
        pattern = int_to_bool_array(i, 3)
        mask.extend(pattern)

    assert len(mask) == 24
    assert all(isinstance(dot, bool) for dot in mask)

    return mask


def is_complete_mask(mask: list[bool]) -> bool:
    """Check if a mask covers all 8 patterns."""
    assert all(
        isinstance(dot, bool) for dot in mask
    ), "Mask must be a list of booleans."

    for i in range(8):
        pattern = int_to_bool_array(i, 3)

        # If `pattern` is not a sub-list of `mask`, then `mask` is not complete.
        found_pattern = False
        for start_idx in range(0, len(mask) - 2):
            if mask[start_idx : start_idx + 3] == pattern:
                found_pattern = True
                break

        if not found_pattern:
            return False

    return True


def count_transitions_in_mask(mask: list[bool]) -> int:
    """Count the number of transitions in a mask."""
    transitions = 0

    for i in range(len(mask) - 1):
        if mask[i] != mask[i + 1]:
            transitions += 1

    return transitions


def test_every_mask(mask_length: int) -> list[list[bool]]:
    """Test every mask of a given length.

    Returns:
        A list of the complete masks found.
    """
    complete_masks = []

    for mask_int in range(2**mask_length):
        mask = int_to_bool_array(mask_int, mask_length)
        if is_complete_mask(mask):
            transition_count = count_transitions_in_mask(mask)
            print(
                f"Found complete mask ({mask_int=}, {mask_length=}, {transition_count=}): {mask}"
            )
            complete_masks.append(mask)

    return complete_masks


def main() -> None:
    naive_mask = make_naive_mask()
    print(f"Naive mask: {naive_mask}")
    assert is_complete_mask(
        naive_mask
    ), "Naive mask is not complete. Error in implementation."
    print("=" * 80)

    for mask_length in range(3, 24):
        mask_list = test_every_mask(mask_length)
        complete_mask_count = len(mask_list)
        print(f"{complete_mask_count=}, {mask_length=}")
        if complete_mask_count > 0:
            break

    print("=" * 80)


if __name__ == "__main__":
    main()
