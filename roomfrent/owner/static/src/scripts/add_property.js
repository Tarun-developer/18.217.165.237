$(document).ready(function() {
    var checkBoxAll = $('#preference1', this);
    var checkBoxfamily = $('#preference2', this);
    var checkBoxgrls = $('#preference3', this);
    var checkBoxbachlor = $('#preference4', this);

    $(checkBoxAll).prop('checked', !checkBoxAll.is(':checked'));
    $(checkBoxfamily).prop('checked', !checkBoxfamily.is(':checked'));
    $(checkBoxgrls).prop('checked', !checkBoxgrls.is(':checked'));
    $(checkBoxbachlor).prop('checked', !checkBoxbachlor.is(':checked'));

    $('#preference1').on('change', function() {
        $(checkBoxfamily).prop('checked', true, !checkBoxfamily.is(':checked'));
        $(checkBoxgrls).prop('checked', true, !checkBoxgrls.is(':checked'));
        $(checkBoxbachlor).prop('checked', true, !checkBoxbachlor.is(':checked'));
    });
    
    $('.property_type_select').on('change', function() {
        var selectedVal = this.value;
        if (selectedVal == 'Boys PG') {
            $(checkBoxbachlor).prop('checked', true, !checkBoxbachlor.is(':checked'));
            $(checkBoxAll).prop('checked', false, !checkBoxAll.is(':checked')).attr("disabled", true);
            $(checkBoxfamily).prop('checked', false, !checkBoxfamily.is(':checked')).attr("disabled", true);
            $(checkBoxgrls).prop('checked', false, !checkBoxgrls.is(':checked')).attr("disabled", true);
        }
        if (selectedVal == 'Girls PG') {
            $(checkBoxAll).prop('checked', false, !checkBoxAll.is(':checked')).attr("disabled", true);
            $(checkBoxfamily).prop('checked', false, !checkBoxfamily.is(':checked')).attr("disabled", true);
            $(checkBoxbachlor).prop('checked', false, !checkBoxbachlor.is(':checked')).attr("disabled", true);
            $(checkBoxgrls).prop('checked', true, !checkBoxgrls.is(':checked'));
        }
        if (!(selectedVal == 'Girls PG' || selectedVal == 'Boys PG')) {
            (checkBoxAll).prop('checked', true, !checkBoxAll.is(':checked')).attr("disabled", false);
            $(checkBoxfamily).prop('checked', true, !checkBoxfamily.is(':checked')).attr("disabled", false);
            $(checkBoxgrls).prop('checked', true, !checkBoxgrls.is(':checked')).attr("disabled", false);
            $(checkBoxbachlor).prop('checked', true, !checkBoxbachlor.is(':checked')).attr("disabled", false);
        }

    })


});