import java.util.*;

public class Sum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter two integer number");
        int n = sc.nextInt(); // 123

        int temp = n; // 123
        int reversed=0; 

        while(n!=0) { // 123 12
            int rem = n % 10; // 3
            reversed = reversed * 10 + rem; // 3
            n = n /10; // 12
        }

        if(temp == reversed)
            System.out.println("This is plaindrome number");
        else
            System.out.println("This is not a palindrome number");

    }
}
// Scanner, System, String
// new: any1thing we create dynamically