function get_input(){
    let product_id=document.getElementById('product_id').value
    $.ajax({
        type : 'POST',
        url: '/product/like/',
        data:{'pid':product_id}
    })

}