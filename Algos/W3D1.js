/* 
    Balance Index

    Here, a balance point is ON an index, not between indices.

    Return the balance index where sums are equal on either side
    (exclude its own value).
    
    Return -1 if none exist.
*/

const nums1 = [2, 5, 1, 2];
const expected1 = 2;

const nums2 = [9, 9];
const expected2 = -1;

/**
 * Finds the balance index in the given array where the sum to the left of the
 *    index is equal to the sum to the right of the index.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The balance index or -1 if there is none.
 */
function balanceIndex(nums) {

    // Construct a while or a for loop, travelling from the left side.
    // Another one for traveling from the right side.
    // These loops do NOT need to be nested, they can be seperate. 

    // One way we can find the middle of an array is dividing the length by 2. (This works primarily for when we have odd numbers, but is not needed!)

    // Sum of the right and sum of the left should have declared values.
    // Use the sums to evaluate that the left and right side are equal.

    // Return the index of the point between the left and right.


}

/*****************************************************************************/