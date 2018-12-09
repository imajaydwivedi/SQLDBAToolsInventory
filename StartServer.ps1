# First we create the request.
$HTTP_Request = [System.Net.WebRequest]::Create('http://localhost:8000')

try {
    # We then get a response from the site.
    $HTTP_Response = $HTTP_Request.GetResponse();

    # We then get the HTTP code as an integer.
    $HTTP_Status = [int]$HTTP_Response.StatusCode

    If ($HTTP_Status -eq 200) {
        Write-Host "Site is OK!"
    }

    # Finally, we clean up the http request by closing it.
    $HTTP_Response.Close()
}
catch {
    Write-Host "The Site may be down, trying to start the site!";
    Set-Location E:\Django\SQLDBAToolsInventory;
    python manage.py runserver;

    return 0; #success
}

