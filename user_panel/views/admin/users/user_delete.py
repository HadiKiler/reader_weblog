from ...imports import *

@login_required
def user_delete(request, id):
    u = get_object_or_404(User, id=id)
    u.delete()
    return redirect(reverse('user_panel_admin_users'))