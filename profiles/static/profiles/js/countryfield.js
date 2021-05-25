// Code taken from the Code Institute walkthrough project
// Boutique Ado: https://github.com/Code-Institute-Solutions/Boutique-Ado

/*jshint esversion: 6 */
// Suggestion found on StackOverflow (https://stackoverflow.com/questions/8852765/jshint-and-jquery-is-not-defined) to bypass replacing the $ with jquery when passing the code into jshint //
/*globals $:false */

let countrySelected = $("id_default_country").val();
if (!countrySelected) {
    $("#id_default_country").css("color", "#AAB7C4");
}
$("#id_default_country").change(function () {
    countrySelected = $(this).val();
    if (!countrySelected) {
        $(this).css("color", "#AAB7C4");
    } else {
        $(this).css("color", "#333333");
    }
});
