def calculator():
    while True:
        print("\nЛаскаво просимо до калькулятора! Оберіть операцію:")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")
        print("5. Вихід")

        try:
            choice = int(input("Номер операції: "))
        except ValueError:
            print("Введіть коректний номер!")
            continue

        if choice == 5:
            print("Дякуємо за використання калькулятора! До побачення!")
            break

        nums = []
        count = 1
        while True:
            entry = input(f"Введіть {count}-е число або 'stop' для завершення: ")
            if entry.lower() == "stop":
                break
            try:
                number = float(entry)
                nums.append(number)
                count += 1
            except ValueError:
                print("Введіть коректне число!")

        if not nums:
            print("Не введено жодного числа.")
            continue

        if choice == 1:
            result = sum(nums)
            print(f"Результат додавання: {result}")
        elif choice == 2:
            result = nums[0]
            for n in nums[1:]:
                result -= n
            print(f"Результат віднімання: {result}")
        elif choice == 3:
            result = 1
            for n in nums:
                result *= n
            print(f"Результат множення: {result}")
        elif choice == 4:
            result = nums[0]
            try:
                for n in nums[1:]:
                    result /= n
                print(f"Результат ділення: {result}")
            except ZeroDivisionError:
                print("Помилка: ділення на нуль!")
        else:
            print("Такої операції немає. Спробуйте ще раз.")

calculator()
