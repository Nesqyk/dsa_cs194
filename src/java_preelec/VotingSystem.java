import java.util.Scanner;

public class VotingSystem {

    public static void main(String[] args) {
        // Set up voting system
        Scanner scanner = new Scanner(System.in);
        boolean runAgain = true;

        // Outer loop to allow multiple voting sessions
        while (runAgain) {
            // Initialize votes array for the candidates: Bob Smith, Carol Davis, Alice Johnson
            int[] votes = new int[3]; 
            boolean voting = true;

            // Display welcome message
            System.out.println("Welcome to the Voting System!");

            // Inner loop for a single voting session
            while (voting) {
                // Display voting menu and candidate list
                System.out.println("\nPlease choose a candidate to vote for:");
                System.out.println("1. Bob Smith");
                System.out.println("2. Carol Davis");
                System.out.println("3. Alice Johnson");
                System.out.println("4. Exit and see results");

                System.out.print("Enter your choice: ");
                
                // Get user choice
                String userInput = scanner.nextLine();
                int choice;

                try {
                    choice = Integer.parseInt(userInput);
                } catch (NumberFormatException e) {
                    choice = 0; // Invalid input
                }

                // Process user input
                switch (choice) {
                    case 1:
                        votes[0]++; // Bob Smith
                        System.out.println("Vote for Bob Smith recorded.");
                        break;
                    case 2:
                        votes[1]++; // Carol Davis
                        System.out.println("Vote for Carol Davis recorded.");
                        break;
                    case 3:
                        votes[2]++; // Alice Johnson
                        System.out.println("Vote for Alice Johnson recorded.");
                        break;
                    case 4:
                        voting = false; // Exit voting session
                        break;
                    default:
                        System.out.println("Invalid choice. Please enter a number from 1 to 4.");
                        break;
                }
            }

            // Voting session ended
            System.out.println("\nVoting session ended. Displaying results...");

            // Display results table
            System.out.println("\n--- Voting Results ---");
            System.out.println("Bob Smith: " + votes[0] + " votes");
            System.out.println("Carol Davis: " + votes[1] + " votes");
            System.out.println("Alice Johnson: " + votes[2] + " votes");

            // Determine max votes and find all candidates with max votes
            int maxVotes = 0;
            for (int voteCount : votes) {
                if (voteCount > maxVotes) {
                    maxVotes = voteCount;
                }
            }
            
            // Announce winner or ties
            System.out.println("\n--- Winner Announcement ---");
            if (maxVotes == 0) {
                System.out.println("No votes were cast in this session.");
            } else {
                int winnerCount = 0;
                String[] candidates = {"Bob Smith", "Carol Davis", "Alice Johnson"};
                StringBuilder winnerNames = new StringBuilder();

                for (int i = 0; i < votes.length; i++) {
                    if (votes[i] == maxVotes) {
                        winnerNames.append(candidates[i]).append(", ");
                        winnerCount++;
                    }
                }
                
                // Remove trailing comma and space
                winnerNames.setLength(winnerNames.length() - 2);

                if (winnerCount > 1) {
                    System.out.println("It's a tie between: " + winnerNames.toString());
                } else {
                    System.out.println("The winner is: " + winnerNames.toString());
                }
            }

            // Ask user to run again
            System.out.print("\nDo you want to run the voting system again? (yes/no): ");
            String runAgainInput = scanner.nextLine().trim().toLowerCase();

            if (!runAgainInput.equals("yes")) {
                runAgain = false;
            }
        }
        
        // Close Scanner and end program
        scanner.close();
        System.out.println("Thank you for using the Voting System. Goodbye!");
    }
}