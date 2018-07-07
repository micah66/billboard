$('#showNewPostFormBtn').click(() => {
  $('#showNewPostForm').addClass('hidden')
  $('#noPostsMessage').addClass('hidden')
  $('#formWrapper').removeClass('hidden')
})

$('#close-form-btn').click(() => {
  $('#showNewPostForm').removeClass('hidden')
  $('#noPostsMessage').removeClass('hidden')
  $('#formWrapper').addClass('hidden')
})

const postPost = () => {
  $.post('/posts/new_post', (newPost) => {
    const postDiv = $('<div/>')
    postDiv.addClass('post')
  })
}
