let btns = document.getElementsByClassName('addtocart')
for(let i = 0; i < btns.length; i++){
    btns[i].addEventListener('click', function(){
        let productId = this.dataset.product
        let action = this.dataset.action
        location.reload()
        console.log(productId)
        if (user === "AnonymousUser"){
            console.log("User is not logged in")
        }
        else{
            updateCart(productId, action)
        }

    })

}
function updateCart(id, action){
    let url = "/home/cart"
    fetch(url, {
        method: 'POST',
        credentials:'same-origin',
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({"productId": id, "action": action})
    })
    .then(response => response.json())
    .then(data => console.log(data))
}

console.log('seef12')