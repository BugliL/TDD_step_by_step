package tests;

// using Junit5.4

import model.Dollar;
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
        Dollar five = new Dollar(5);
        Dollar ten = five.times(2);
        assertEquals(new Dollar(10), ten);
        Dollar fifthteen = five.times(3);
        assertEquals(new Dollar(15), fifthteen);
    }

    @Test
    @DisplayName("When compared to another 5 dollar, result equal")
    public void test_equality(){
        assertEquals(new Dollar(5), new Dollar(5));
        assertTrue(new Dollar(5).equals(new Dollar(5)));
    }

}
