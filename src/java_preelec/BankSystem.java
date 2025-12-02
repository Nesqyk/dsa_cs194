import java.util.Scanner;

public class BankSystem {

    // BankAccount class definition
    public static class BankAccount {
        private String holderName;
        private double balance;

        public BankAccount(String holderName, double balance) {
            this.holderName = holderName;
            this.balance = balance;
        }

        public void deposit(double amount) {
            if (amount > 0) {
                this.balance += amount;
                System.out.println("\nSuccessfully deposited $" + String.format("%.2f", amount) + ".");
            } else {
                System.out.println("\nError: Deposit amount must be positive.");
            }
        }

        public void withdraw(double amount) {
            if (amount <= 0) {
                System.out.println("\nError: Withdrawal amount must be positive.");
            } else if (amount > this.balance) {
                System.out.println("\nError: Insufficient funds. Your current balance is $" + String.format("%.2f", this.balance) + ".");
            } else {
                this.balance -= amount;
                System.out.println("\nSuccessfully withdrew $" + String.format("%.2f", amount) + ".");
            }
        }

        public double getBalance() {
            return balance;
        }

        public String getHolderName() {
            return holderName;
        }
    }

    // Main method for the menu-driven application
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        BankAccount account = null; // Initialize as null to check if an account exists

        System.out.println("Welcome to the Bank of CIS!");

        while (true) {
            System.out.println("\n--- Main Menu ---");
            if (account == null) {
                System.out.println("1. Open an Account");
            } else {
                System.out.println("Current Account Holder: " + account.getHolderName());
                System.out.println("2. Deposit Funds");
                System.out.println("3. Withdraw Funds");
                System.out.println("4. Check Balance");
            }
            System.out.println("5. Exit");
            System.out.print("Please enter your choice: ");

            String choiceStr = scanner.nextLine();
            int choice;
            try {
                choice = Integer.parseInt(choiceStr);
            } catch (NumberFormatException e) {
                System.out.println("\nInvalid input. Please enter a number from the menu.");
                continue;
            }

            if (account == null && choice != 1 && choice != 5) {
                System.out.println("\nPlease open an account first.");
                continue;
            }

            switch (choice) {
                case 1:
                    if (account == null) {
                        System.out.print("Enter your name: ");
                        String name = scanner.nextLine();
                        System.out.print("Enter your initial deposit: ");
                        double initialDeposit;
                        try {
                            initialDeposit = Double.parseDouble(scanner.nextLine());
                            if (initialDeposit < 0) {
                                System.out.println("\nInitial deposit cannot be negative. Setting to $0.00.");
                                initialDeposit = 0.0;
                            }
                        } catch (NumberFormatException e) {
                            System.out.println("\nInvalid input for deposit. Setting to $0.00.");
                            initialDeposit = 0.0;
                        }
                        account = new BankAccount(name, initialDeposit);
                        System.out.println("\nAccount successfully opened for " + account.getHolderName() + "!");
                    } else {
                        System.out.println("\nAn account is already open. Please use other options.");
                    }
                    break;
                case 2:
                    System.out.print("Enter deposit amount: ");
                    try {
                        double depositAmount = Double.parseDouble(scanner.nextLine());
                        account.deposit(depositAmount);
                    } catch (NumberFormatException e) {
                        System.out.println("\nInvalid amount entered. Please enter a number.");
                    }
                    break;
                case 3:
                    System.out.print("Enter withdrawal amount: ");
                    try {
                        double withdrawAmount = Double.parseDouble(scanner.nextLine());
                        account.withdraw(withdrawAmount);
                    } catch (NumberFormatException e) {
                        System.out.println("\nInvalid amount entered. Please enter a number.");
                    }
                    break;
                case 4:
                    System.out.println("\nYour current balance is: $" + String.format("%.2f", account.getBalance()));
                    break;
                case 5:
                    System.out.println("\nThank you for banking with us. Goodbye!");
                    scanner.close();
                    return;
                default:
                    System.out.println("\nInvalid choice. Please select a valid option from the menu.");
            }
        }
    }
}
