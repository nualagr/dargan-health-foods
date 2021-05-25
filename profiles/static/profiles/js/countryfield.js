// Code taken from the Code Institute walkthrough project
// Boutique Ado: https://github.com/Code-Institute-Solutions/Boutique-Ado
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
