def babble_sort(element_list):
    d=0
    for i in range(len(element_list)):
        for j in range(i+1, len(element_list)):
            a, b = element_list[i], element_list[j]
            if a > b:
                element_list[i], element_list[j] = b, a
    return element_list








element_list = [45,23,1,67,98,56,43,55,78,42,66,76,91,69,33,44,4,2,6,0,109]
names = [
    # USA
    "Emma", "Liam", "Olivia", "Noah", "Ava", "Elijah", "Sophia", "James", "Isabella", "William",
    # UK
    "Oliver", "George", "Harry", "Jack", "Jacob", "Charlie", "Thomas", "Henry", "Olivia", "Amelia",
    # Canada
    "Liam", "Emma", "Noah", "Olivia", "Jackson", "Charlotte", "Aiden", "Ava", "Lucas", "Sophia",
    # Australia
    "Oliver", "Charlotte", "William", "Olivia", "Jack", "Mia", "Noah", "Amelia", "Henry", "Isla",
    # India
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Reyansh", "Ayaan", "Krishna", "Ishaan",
    "Aarohi", "Anaya", "Diya", "Myra", "Aadhya", "Anika", "Saanvi", "Prisha", "Riya", "Anvi",
    # Bangladesh
    "Arif", "Sadia", "Hasan", "Nusrat", "Tanvir", "Mehedi", "Nazia", "Rafi", "Shakil", "Taslima",
    "Amin", "Farzana", "Imran", "Jahanara", "Kamal", "Lamia", "Mamun", "Nabila", "Omar", "Parvin",
    # China
    "Wei", "Fang", "Jie", "Li", "Chen", "Wang", "Hua", "Lin", "Zhang", "Yang",
    "Liu", "Zhao", "Sun", "Wu", "Zhu", "Hu", "Gao", "Ma", "Guo", "He",
    # Japan
    "Haruto", "Yui", "Yuto", "Hina", "Sota", "Rin", "Yuki", "Mio", "Sora", "Riko",
    # South Korea
    "Seo-Jun", "Ha-Yoon", "Do-Yun", "Seo-Yeon", "Ji-Ho", "Ji-A", "Ha-Jun", "Ji-Woo", "Joon-Woo", "Ha-Eun",
    # Uganda
    "Abdullah", "Kamali", "Nalubega", "Kato", "Nakato", "Mukasa", "Nabukeera", "Ssebunya", "Mugerwa", "Nabirye",
    # Nigeria
    "Emeka", "Ngozi", "Chinedu", "Chiamaka", "Chibuzo", "Adaeze", "Obinna", "Chijioke", "Ifeoma", "Kelechi",
    # Mexico
    "Santiago", "Valentina", "Mateo", "Regina", "Sebastián", "Victoria", "Leonardo", "María", "Matías", "Ximena",
    # Brazil
    "Miguel", "Alice", "Arthur", "Sophia", "Heitor", "Helena", "Bernardo", "Valentina", "Davi", "Laura",
    # Russia
    "Aleksandr", "Anastasia", "Dmitry", "Maria", "Maxim", "Elena", "Ivan", "Olga", "Kirill", "Natalia",
    # France
    "Gabriel", "Jade", "Louis", "Louise", "Raphaël", "Emma", "Jules", "Alice", "Lucas", "Chloé",
    # Italy
    "Leonardo", "Sofia", "Francesco", "Giulia", "Alessandro", "Aurora", "Lorenzo", "Ginevra", "Mattia", "Emma",
    # Germany
    "Ben", "Emma", "Paul", "Mia", "Finn", "Hanna", "Elias", "Sophia", "Jonas", "Emilia",
    # Spain
    "Hugo", "Lucía", "Martín", "Sofía", "Lucas", "Martina", "Mateo", "María", "Leo", "Julia",
    # Portugal
    "Santiago", "Francisca", "João", "Matilde", "Martim", "Beatriz", "Afonso", "Leonor", "Tomás", "Carolina"
]
print(f"Sorted element list {babble_sort(names)}")