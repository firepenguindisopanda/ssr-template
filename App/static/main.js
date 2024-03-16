
async function getUserData(){
    const response = await fetch('/api/users');
    return response.json();
}

async function getIdentity(){
    const response = await fetch('/api/identify');
    if (!response.ok) {
        // If response status is not ok (e.g., unauthorized), throw a custom error
        throw new Error('Unauthorized: You do not have permission to access this resource.');
    }
    // Otherwise, return the response
    return response.json();
}

function loadTable(users){
    const table = document.querySelector('#result');
    for(let user of users){
        table.innerHTML += `<tr>
            <td>${user.id}</td>
            <td>${user.username}</td>
        </tr>`;
    }
}

async function main(){
    try {
        const users = await getUserData();
        loadTable(users);
        // Check if the user is logged in before displaying the Identify link
        const response = await fetch('/api/identify');
        const isLoggedIn = response.ok;
        if (!isLoggedIn) {
            // If the user is not logged in, hide the Identify link
            document.getElementById('identify-link').style.display = 'none';
        }else{
            document.getElementById('identify-link').style.display = 'block';
        }
    } catch (error) {
        // Catch any errors thrown during getUserData or getIdentity calls
        console.error(error); // Log the error to the console (optional)
        // Display a custom error message to the user
    }
}

main();