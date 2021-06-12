$(document).ready(
    function()
    {
        $("#signform").submit(
            function()
            { 
                if ($("#pass").val() === $("#cpass").val())
                {
                    return true;
                }
                else
                {
                    $("#passmsg").css("display","block");
                    $("#passmsg").text("password and confirm password not matched");
                    return false;
                }
            }
        )
    }
)