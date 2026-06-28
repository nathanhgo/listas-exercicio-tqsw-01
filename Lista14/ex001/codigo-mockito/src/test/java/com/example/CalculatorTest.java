package com.example;
import org.junit.Test;
import org.mockito.Mockito;
import static org.junit.Assert.assertThrows;

public class CalculatorTest {

    @Test
    public void testDivideByZero() {
       Calculator calculator = Mockito.mock(Calculator.class);
       
       Mockito.when(calculator.divide(Mockito.anyInt(), Mockito.eq(0)))
              .thenThrow(new ArithmeticException("Division by zero"));
       
       assertThrows(ArithmeticException.class, () -> calculator.divide(10, 0));
    }
}
