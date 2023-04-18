class Calculator {
    public int add(int n1, int n2) {
        return n1 + n2;
    }
}

public class ClassObject {
    public static void main(String args[]) {
        int n1 = 4;
        int n2 = 10;

        Calculator calc = new Calculator();
        
        int result = calc.add(n1, n2);
        System.out.println(result);
    }
}

// Object Oriented Programming
// Object => properties & behaviour
// Class => properties of the object

// Code -compile-> JDK -run-> JVM(Byte Code) -> 
