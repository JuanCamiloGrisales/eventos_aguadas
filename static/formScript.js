document.addEventListener('DOMContentLoaded', function () {
    function toggleDisabled(field, condition) {
        if (condition) {
            field.value = '';
            field.disabled = true;
        } else {
            field.disabled = false;
        }
    }

    var todoElDiaCheckbox = document.querySelector('#id_todo_el_dia');
    var desdeField = document.querySelector('#id_desde');
    var hastaField = document.querySelector('#id_hasta');
    var cuposIlimitadosCheckbox = document.querySelector('#id_cupos_ilimitados');
    var cuposMaximosField = document.querySelector('#id_cupos_maximos');

    todoElDiaCheckbox.addEventListener('change', function () {
        toggleDisabled(desdeField, this.checked);
        toggleDisabled(hastaField, this.checked);
    });

    cuposIlimitadosCheckbox.addEventListener('change', function () {
        toggleDisabled(cuposMaximosField, this.checked);
    });
});