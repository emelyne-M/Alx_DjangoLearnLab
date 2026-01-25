# LibraryProject - Custom User and Permissions

## Project Overview
LibraryProject is a Django application that demonstrates **custom user model implementation**, **user groups**, and **permissions management**. The project simulates a library system where different users (Admins, Editors, Viewers) have **role-based access control** to perform actions like viewing, creating, editing, or deleting books and library data.

This project is built as part of the **ALX Advanced Features and Security task**.

---

## Features Implemented

1. **Custom User Model**
   - Located in `bookshelf/models.py`
   - Extends Django’s `AbstractUser`
   - Additional fields added:
     - `date_of_birth`
     - `profile_photo`
   - `AUTH_USER_MODEL` updated in `LibraryProject/settings.py`:
     ```python
     AUTH_USER_MODEL = 'bookshelf.CustomUser'
     ```

2. **Custom User Manager**
   - `CustomUserManager` in `bookshelf/models.py`
   - Methods implemented:
     - `create_user()`
     - `create_superuser()`

3. **Permissions**
   - Custom model permissions added:
     - `can_view`
     - `can_create`
     - `can_edit`
     - `can_delete`
   - Example in `bookshelf/models.py`:
     ```python
     class Book(models.Model):
         title = models.CharField(max_length=255)
         ...
         class Meta:
             permissions = [
                 ("can_view", "Can view book"),
                 ("can_create", "Can create book"),
                 ("can_edit", "Can edit book"),
                 ("can_delete", "Can delete book"),
             ]
     ```

4. **Groups**
   - Groups created via a **custom management command**:
     - `Admins` → full access
     - `Editors` → can create and edit
     - `Viewers` → can view only
   - Command: `python manage.py setup_groups`

5. **Permission Enforcement**
   - Views check permissions using Django decorators:
     ```python
     @permission_required('bookshelf.can_edit', raise_exception=True)
     def edit_book(request, book_id):
         ...
     ```
   - Ensures users cannot access or modify resources without proper permissions.

---

