class A {
    public void f() {System.out.println("1");}
    public static void g() {System.out.println("2");}

}

class B extends A {
    public void f() { System.out.println("3");}
}

class C extends B {
    public static void g() {System.err.println("4");}
}

public class Test {

    public static void main(String[] args) {
        A objc = new C();

        objc.f();
        objc.g();
        C my = (C)objc;
        my.g();
    }
}
