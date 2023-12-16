def is_valid_five_digits(input_str):
    return input_str.isdigit() and len(input_str) == 5

def baby_weight_program():
    # Lists to store all baby data and parent data
    all_babies_data = []
    all_parents_data = []

    while True:
        # Interaction with the parent to gather information
        baby_data = {}
        baby_data['baby_first_name'] = input("Parent: What is your baby's first name? ")
        baby_data['baby_last_name'] = input("Parent: What is your baby's last name? ")
        baby_data['date_of_birth'] = input("Parent: What is your baby's date of birth? (Format: DD/MM/YYYY) ")
        baby_data['baby_gender'] = input("Parent: Is your baby male or female? ")
        baby_data['height'] = float(input("Parent: How tall is your baby (in centimeters)? "))

        # Check if both first name and last name are provided
        if not baby_data['baby_first_name'] or not baby_data['baby_last_name']:
            print("Parent: Please provide both first name and last name for your baby.")
            continue

        # Display gathered information
        print("\nBaby Information:")
        for key, value in baby_data.items():
            print(f"{key.replace('_', ' ').title()}: {value}")

        # Check the baby's weight
        baby_data['baby_weight'] = float(input("\nParent: How much does your baby weigh (in kilograms)? "))

        # Decision based on baby's weight
        if baby_data['baby_weight'] > 40:
            print(f"\nDoctor: The baby's weight is above 40 kilograms.")
            print("Doctor: The baby will need to stay in the hospital for a nutritional checkup of 10 days.")

            # Request insurance information if the baby needs to stay
            parent_data = {}
            parent_data['parent_first_name'] = input("Parent: What is your first name? ")
            parent_data['parent_last_name'] = input("Parent: What is your last name? ")
            parent_data['insurance_provider_name'] = input("Parent: What is your insurance provider's name? ")
            parent_data['baby_insurance_provider_name'] = input("Parent: What is your baby's insurance provider's name? ")
            parent_data['parent_insurance_number'] = input("Parent: Please enter your insurance number (5 digits): ")
            parent_data['baby_insurance_number'] = input("Parent: Please enter your baby's insurance number (5 digits): ")

            # Check if insurance numbers are valid 5-digit numbers
            if not (is_valid_five_digits(parent_data['parent_insurance_number']) and is_valid_five_digits(parent_data['baby_insurance_number'])):
                print("Nurse: Please ensure both parent and baby insurance numbers are 5 unique digits. Restarting the process.")
                continue

            # Check if parent's insurance number matches baby's insurance number and if insurance companies are the same
            if parent_data['parent_insurance_number'] == parent_data['baby_insurance_number'] and parent_data['insurance_provider_name'] == parent_data['baby_insurance_provider_name']:
                # Nurse appointment and questions
                print("\nNurse: A nurse will be appointed to you to discuss your baby's health conditions.")
                print("Nurse: Let me ask you a few true/false questions.")

                # Questions for the parent
                questions = [
                    "1. Your baby has a regular health checkup schedule.",
                    "2. Your baby has specific likes or dislikes for certain foods.",
                    "3. Your baby has experienced recent changes in health or behavior.",
                    "4. Your baby has known allergies or sensitivities.",
                    "5. You have specific concerns or observations about your baby's health."
                ]

                # Ask questions and check responses
                all_questions_answered = all(input(f"Parent: {question} (true/false) ") in ['true', 'false'] for question in questions)

                # Final message based on responses
                if all_questions_answered:
                    print("\nNurse: Thank you! We will need to see you every day for the best care of your baby.")
                else:
                    print("\nNurse: Please answer all questions with 'true' or 'false' for the well-being of your baby.")
            else:
                print("Nurse: Insurance information does not match. Please ensure the information is correct. Restarting the process.")
                continue

        else:
            print(f"\nDoctor: The baby's weight is below 40 kilograms.")
            print("Doctor: It's important to ensure your baby gets the right nutrition. Here are some eating patterns to follow:")
            print("1. Include a variety of fruits and vegetables in your baby's diet.")
            print("2. Offer small and frequent meals throughout the day.")
            print("3. Introduce age-appropriate cereals and grains.")
            print("4. Ensure your baby gets enough fluids, such as breast milk or formula.")
            print("5. Consult with a pediatrician for personalized advice based on your baby's needs.")
            print("Parent: Please follow these patterns for the best health of your baby.")
            print("Doctor: We recommend regular check-ups to monitor your baby's progress.")

            # Initialize parent_data here to avoid UnboundLocalError
            parent_data = {}

        # Store baby data and parent data
        all_babies_data.append(baby_data)
        all_parents_data.append(parent_data)

        # Ask if the parent wants to continue
        continue_input = input("\nParent: Do you want to input information for another baby? (yes/no) ")
        if continue_input.lower() != 'yes':
            break

    # Display all stored data
    print("\nAll Babies' Data:")
    for baby_data in all_babies_data:
        for key, value in baby_data.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        print()

    print("\nAll Parents' Data:")
    for parent_data in all_parents_data:
        for key, value in parent_data.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        print()

# Run the baby weight program
baby_weight_program()