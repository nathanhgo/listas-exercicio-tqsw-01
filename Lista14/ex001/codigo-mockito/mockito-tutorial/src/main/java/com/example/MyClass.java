package com.example;
public class MyClass {
    private MyDependency dependency;

    public MyClass() {}
    public MyClass(MyDependency dependency) { this.dependency = dependency; }

    public String publicMethod() { return privateMethod(); }
    private String privateMethod() { return "RealPrivate"; }

    public static String staticMethod(String input) { return "RealStatic"; }
    public String getDependencyValue() { return dependency.getDependencyValue(); }
}
