$(document).ready(function() {
    // Bind on continent field change
    $(':input[name$=type]').on('change', function() {
        // Get the field prefix, ie. if this comes from a formset form
        var prefix = $(this).getFormPrefix();

        // Clear the autocomplete with the same prefix
        $(':input[name=' + prefix + 'code]').val(null).trigger('change');
    });
});
