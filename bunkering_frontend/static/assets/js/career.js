$(document).ready(function () {
    const bdPhoneRegex = /^\+8801[3-9]\d{8}$/;

    let $mobileSelector = $("#mobile");
    let $nameSelector = $("#name");
    let $emailSelector = $("#email");

    $mobileSelector.on("blur", function () {
        const mobile = $(this).val().trim();
        if (!bdPhoneRegex.test(mobile)) {
            $(this).addClass("is-invalid");
        } else {
            $(this).removeClass("is-invalid").addClass("is-valid");
        }
    });

    $("form").on("submit", function (e) {
        let mobile = $mobileSelector.val().trim();
        let name = $nameSelector.val().trim();
        let email = $emailSelector.val().trim();

        $nameSelector.removeClass("is-invalid");
        $mobileSelector.removeClass("is-invalid");
        $emailSelector.removeClass("is-invalid");

        let isValid = true;

        if (!name) {
            $nameSelector.addClass("is-invalid");
            isValid = false;
        }

        if (!email) {
            $emailSelector.addClass("is-invalid");
            isValid = false;
        }

        if (!bdPhoneRegex.test(mobile)) {
            e.preventDefault();  // Prevent form submission
            $mobileSelector.addClass("is-invalid").focus();
            isValid = false;
        }
        if (!isValid) {
            e.preventDefault();
        }
    });
});
