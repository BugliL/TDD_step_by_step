package tests;

// using Junit5.4

import model.Dollar;
import model.Franc;
import model.Money;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("Given 5 franc")
public class FrancTest {

    @Test
    @DisplayName("When multiplied by 2 result 10 and by 3 result 15")
    public void test_multiplication() {
        Money five = Money.franc(5);
        Money ten = five.times(2);
        assertEquals(Money.franc(10), ten);
        Money fifthteen = five.times(3);
        assertEquals(Money.franc(15), fifthteen);
    }

    @Test
    @DisplayName("When compared to another 5 franc, result equal")
    public void test_equality() {
        assertEquals(Money.franc(5), Money.franc(5));
        assertNotEquals(Money.franc(5), Money.franc(15));
    }

}
