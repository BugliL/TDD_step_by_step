package tests;

// using Junit5.4

import model.Money;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

//
//  Todo:
//     $5 + 10 CHF = $10 if CHF:USD is 2:1
//     $5 * 2 = $10
//     Dollar side-effects?
//     Money rounding?

@DisplayName("Given 5 dollars")
public class DollarTest {

    @Test
    @DisplayName("When multiplied by 2 result 10 and by 3 result 15")
    public void test_multiplication() {
        Money five = Money.dollar(5);
        Money ten = five.times(2);
        assertEquals(Money.dollar(10), ten);
        Money fifthteen = five.times(3);
        assertEquals(Money.dollar(15), fifthteen);
    }

    @Test
    @DisplayName("When compared to another 5 dollar, result equal")
    public void test_equality() {
        assertEquals(Money.dollar(5), Money.dollar(5));
        assertNotEquals(Money.dollar(5), Money.dollar(15));
    }

}
