class RtsLabs:

    def aboveBelow(self, nums: list[int], comparison: int) -> dict:
        above = 0
        below = 0

        for num in nums:
            if num > comparison:
                above += 1
            elif num < comparison:
                below += 1

            # no else because we have no specs for num == comparison

        return {'above': above, 'below': below}

    def stringRotation(self, orig_string: str, rotation_amount: int) -> str:

        # rotation_amount must be an integer
        if not isinstance(rotation_amount, int):
            raise RuntimeError(f'{rotation_amount} is not an integer!')

        # rotation_amount must be greater than 0
        if rotation_amount <= 0:
            raise RuntimeError(f'{rotation_amount} is not positive!')

        return (
            f'{orig_string[rotation_amount * -1:]}'
            f'{orig_string[:rotation_amount * -1]}'
        )

if __name__ == '__main__':
    rts = RtsLabs()

    aboveBelow_results = rts.aboveBelow(
        [1, 5, 2, 1, 10],
        6
    )
    print(f'above below: {aboveBelow_results}')


    stringRotation_results = rts.stringRotation('MyString', 2)
    print(f'string rotation: {stringRotation_results}')