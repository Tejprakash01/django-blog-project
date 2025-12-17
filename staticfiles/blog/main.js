// HELPER FUNCTION TO GET CSRF TOKEN

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie("csrftoken");
// LIKE POST
document.addEventListener("click", function (e) {
  if (e.target.closest(".like-btn")) {
    const btn = e.target.closest(".like-btn");
    const postId = btn.dataset.postId;

    fetch(`/like/${postId}/`, {
      method: "POST",
      headers: {
        "X-CSRFToken": getCookie("csrftoken"),
      },
    })
      .then(res => res.json())
      .then(data => {
        document.getElementById(`like-count-${postId}`).innerText =
          data.likes_count;
      });
  }
});

  // ADD COMMENT
document.addEventListener("submit", function (e) {
  if (e.target.classList.contains("comment-form")) {
    e.preventDefault();

    const form = e.target;
    const postId = form.dataset.postId;
    const input = form.querySelector("input[name='text']");
    const text = input.value.trim();
    const csrfToken = form.querySelector("[name=csrfmiddlewaretoken]").value;

    if (!text) return;

    fetch(`/comment/add/${postId}/`, {
      method: "POST",
      headers: {
        "X-CSRFToken": csrfToken,
        "X-Requested-With": "XMLHttpRequest",
      },
      body: new URLSearchParams({ text }),
    })
      .then(res => res.json())
      .then(data => {
        if (data.error) return;

        const commentsDiv = document.getElementById(`comments-${postId}`);

        commentsDiv.insertAdjacentHTML("beforeend", `
          <div class="comment">
            <strong>${data.user}</strong>: ${data.text}
          </div>
        `);

        input.value = "";
      });
  }
});

/* DELETE COMMENT */
document.addEventListener("click", function (e) {
  if (e.target.classList.contains("comment-delete-btn")) {
    const commentId = e.target.dataset.commentId;

    fetch(`/comment/delete/${commentId}/`, {
      method: "POST",
      headers: {
        "X-CSRFToken": "{{ csrf_token }}",
      },
    })
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        document.getElementById(`comment-${commentId}`).remove();
      }
    });
  }
});
