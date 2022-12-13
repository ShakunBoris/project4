document.addEventListener("DOMContentLoaded", function () {
  const follow = document.querySelector("#follow-button");
  if (follow) {follow.addEventListener("click", folUnfol)}
});

function folUnfol() {
    // Fetch PUT to renew DB and button
    // console.log(this.dataset.profile)
    fetch(`/user/${this.dataset.profile}`, {
        method: 'PUT',
        body: JSON.stringify({
            folUnfol: true,  
        })
    }).then(() => {
    if (document.querySelector('#follow-button').innerHTML == 'Follow') {
        document.querySelector('#follow-button').innerHTML = 'Unfollow'
        console.log('REMOVING')
    } else {
        document.querySelector('#follow-button').innerHTML = 'Follow'
        console.log('ADDING')
    }
    })
}