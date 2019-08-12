package tests;

// using Junit5.4

import model.Dollar;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

//
//  Todo:
//     $5 + 10 CHF = $10 if CHF:USD is 2:1
//     $5 * 2 = $10
//     Dollar side-effects?
//     Money rounding?

public class DollarTest {

    @Test
    public void given_5_Dollar_when_multiplied_by_3_and_2_than_result_15() {
        Dollar five = new Dollar(5);
        Dollar ten = five.times(2);
        assertEquals(new Dollar(10), ten);
        Dollar fifthteen = five.times(3);
        assertEquals(new Dollar(15), fifthteen);
    }

    @Test
    public void given_2_dollers_of_same_amount_when_compared_result_equal(){
        assertEquals(new Dollar(5), new Dollar(5));
        assertTrue(new Dollar(5).equals(new Dollar(5)));
    }

}
