/* 
    Given a string containing space separated words
    Reverse each word in the string.

    If you need to, use .split to start, then try to do it without.
*/

const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */
function reverseWords(str) {
    // Using split, we can seperate the strings into individual values. https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split
    // Identifying spaces within the string, using split.
    // Using a for loop to traverse the string. We could start from the right, traversing to the left.

    let reversed = '';
    // After looping through the given string, we can concatenate it to our reversed variable.


    return reversed
}

/*****************************************************************************/

/* 
    Reverse Word Order

    Given a string of words (with spaces)
    return a new string with words in reverse sequence.
*/

const str1_1 = "This is a test";
const expected1_1 = "test a is This";

const str2_1 = "hello";
const expected2_1 = "hello";

const str3_1 = "   This  is a   test  ";
const expected3_1 = "test a is This";

/**
 * Reverses the order of the words but not the words themselves form the given
 * string of space separated words.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string containing space separated words.
 * @returns {string} The given string with the word order reversed but the words
 *    themselves are not reversed.
 */
function reverseWordOrder(wordsStr) {

    let words = wordsStr.split(' ');
    console.log(words)
    // Loop in reverse order with the array from the split method.
    let temp = ''
    // Add each word in reverse order to our temp string with concatenation
    // Possibly add the spaces back to the string as they are added? 

}

reverseWordOrder(str1_1)

/*****************************************************************************/