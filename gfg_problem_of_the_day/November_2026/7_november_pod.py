
class Solution:
    def generateUsernames(self, arr: list[str]) -> list[str]:
        # Store all initially reserved usernames
        reserved = set(arr)

        # Store usernames that have already been assigned
        used = set()

        # Store the next suffix to try for each username
        suffix = {}

        ans = []

        for name in arr:

            # If username is not already assigned
            if name not in used:
                used.add(name)
                ans.append(name)

            else:
                # Start checking from the next available suffix
                i = suffix.get(name, 1)

                while name + str(i) in reserved or name + str(i) in used:
                    i += 1

                new_name = name + str(i)

                # Assign the generated username
                ans.append(new_name)
                used.add(new_name)

                # Update the next suffix
                suffix[name] = i + 1

        return ans
