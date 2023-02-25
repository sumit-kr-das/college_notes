
class Calculator //creating Calculator class
{
    public int add(int pritam1, int pritam2, int pritam3) //class method1
    {
        return pritam1 + pritam2 + pritam3;
    }

    public int add(int pritam1, int pritam2) //method2 with same name
    {
        return pritam1 + pritam2;
    }

}

public class Demo { 
    public static void main(String a[]) {
        int ami = 10;
        int sha = 15;
        int tmi = 20;
        //creating object
        Calculator cal = new Calculator();
        //int result = cal.add(ami, tmi);
        int result3 = cal.add(ami, tmi, sha);
        int result4 = cal.add(ami, tmi);
        //System.out.println(result);
        System.out.println(result3);
        System.out.println(result4);
    }
}