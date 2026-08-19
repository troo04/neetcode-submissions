class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        accounts = {}
        invalid = set()

        for i, t in enumerate(transactions):
            name, time, amt, city = t.split(",")
            amt = int(amt)
            time = int(time)

            if name not in accounts:
                accounts[name] = [(time, amt, city, i)]

            if amt > 1000:
                invalid.add(i)

            ## check if invalid

            for prev_time, prev_amt, prev_city, prev_i in accounts[name]:
                if abs(time - prev_time) <= 60 and city != prev_city:
                    invalid.add(i)
                    invalid.add(prev_i)

            accounts[name].append((time, amt, city, i))
            
        return [t for i, t in enumerate(transactions) if i in invalid]