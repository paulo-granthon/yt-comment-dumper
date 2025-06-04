def build_comment_tree(comments):
    comment_dict = {comment['comment_id']: comment for comment in comments}
    tree = []

    for comment in comments:
        parent_id = comment.get('parent_id')
        if parent_id:
            parent = comment_dict.get(parent_id)
            if parent:
                parent.setdefault('replies', []).append(comment)
        else:
            tree.append(comment)

    return tree
