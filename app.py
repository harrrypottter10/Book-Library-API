import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="Book Library",
    page_icon="📚",
    layout="wide"
)


# --------------------------------
# Session State
# --------------------------------

if "selected_book" not in st.session_state:
    st.session_state.selected_book = None

if "show_add" not in st.session_state:
    st.session_state.show_add = False


# --------------------------------
# Functions
# --------------------------------

def get_books(search=""):

    if search:
        response = requests.get(
            f"{API_URL}/search",
            params={"title": search}
        )
    else:
        response = requests.get(
            f"{API_URL}/"
        )

    if response.status_code == 200:
        return response.json()

    return []


# --------------------------------
# Header
# --------------------------------

st.title("📚 Book Library")

st.write("Find your favorite books")


# --------------------------------
# Search + Add Book
# --------------------------------

col1, col2 = st.columns([5, 1])

with col1:

    search = st.text_input(
        "🔍 Search",
        placeholder="Search books by name...",
        label_visibility="collapsed"
    )

with col2:

    if st.button("➕ Add Book", use_container_width=True):

        st.session_state.show_add = True
        st.session_state.selected_book = None


# --------------------------------
# Add Book
# --------------------------------

if st.session_state.show_add:

    st.subheader("➕ Add New Book")

    col1, col2 = st.columns(2)

    with col1:

        title = st.text_input("Book Name")
        author = st.text_input("Author")
        genre = st.text_input("Genre")

    with col2:

        year = st.number_input(
            "Year",
            min_value=1001,
            step=1
        )

        in_stock = st.checkbox(
            "In Stock",
            value=False
        )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "Add Book",
            use_container_width=True
        ):

            if not title or not author or not genre:

                st.warning(
                    "Please fill all fields."
                )

            else:

                data = {
                    "title": title,
                    "author": author,
                    "genre": genre,
                    "year": year,
                    "in_stock": in_stock
                }

                response = requests.post(
                    f"{API_URL}/",
                    json=data
                )

                if response.status_code == 200:

                    st.success(
                        "Book added successfully!"
                    )

                    st.session_state.show_add = False
                    st.rerun()

                else:

                    st.error(
                        response.text
                    )

    with col2:

        if st.button(
            "Cancel",
            use_container_width=True
        ):

            st.session_state.show_add = False
            st.rerun()


# --------------------------------
# Selected Book Details
# --------------------------------

if st.session_state.selected_book:

    book = st.session_state.selected_book

    st.divider()

    if st.button("← Back to Books"):

        st.session_state.selected_book = None
        st.rerun()

    st.header(f"📖 {book['title']}")

    st.write(f"**Author:** {book['author']}")
    st.write(f"**Genre:** {book['genre']}")
    st.write(f"**Year:** {book['year']}")

    if book["in_stock"]:
        st.success("In Stock: ✅ Yes")
    else:
        st.error("In Stock: ❌ No")

    st.caption(f"Book ID: {book['id']}")

    st.divider()

    # --------------------------------
    # Edit and Delete Buttons
    # --------------------------------

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "✏️ Edit Book",
            use_container_width=True
        ):

            st.session_state.edit_book = True
            st.rerun()

    with col2:

        if st.button(
            "🗑️ Delete Book",
            use_container_width=True
        ):

            response = requests.delete(
                f"{API_URL}/{book['id']}"
            )

            if response.status_code == 200:

                st.success(
                    "Book deleted successfully!"
                )

                st.session_state.selected_book = None
                st.session_state.edit_book = False

                st.rerun()

            else:

                st.error(response.text)


    # --------------------------------
    # Edit Form
    # --------------------------------

    if st.session_state.get("edit_book", False):

        st.divider()

        st.subheader("✏️ Edit Book")

        edit_title = st.text_input(
            "Book Name",
            value=book["title"]
        )

        edit_author = st.text_input(
            "Author",
            value=book["author"]
        )

        edit_genre = st.text_input(
            "Genre",
            value=book["genre"]
        )

        edit_year = st.number_input(
            "Year",
            min_value=1001,
            value=book["year"],
            step=1
        )

        edit_stock = st.checkbox(
            "In Stock",
            value=book["in_stock"]
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "💾 Save Changes",
                use_container_width=True
            ):

                data = {
                    "title": edit_title,
                    "author": edit_author,
                    "genre": edit_genre,
                    "year": edit_year,
                    "in_stock": edit_stock
                }

                response = requests.put(
                    f"{API_URL}/{book['id']}",
                    json=data
                )

                if response.status_code == 200:

                    st.success(
                        "Book updated successfully!"
                    )

                    st.session_state.selected_book = None
                    st.session_state.edit_book = False

                    st.rerun()

                else:

                    st.error(response.text)

        with col2:

            if st.button(
                "Cancel",
                use_container_width=True
            ):

                st.session_state.edit_book = False
                st.rerun()


# --------------------------------
# Show Books
# --------------------------------

else:

    st.divider()

    if search:

        st.subheader(
            f"🔍 Search results for: {search}"
        )

    else:

        st.subheader("📚 All Books")

    books = get_books(search)

    if not books:

        st.info(
            "No books found."
        )

    else:

        # Create 4 columns like an ecommerce store

        columns = st.columns(4)

        for index, book in enumerate(books):

            with columns[index % 4]:

                st.markdown(
                    "### 📖"
                )

                st.subheader(
                    book["title"]
                )

                st.write(
                    f"**Author:** {book['author']}"
                )

                st.write(
                    f"**Genre:** {book['genre']}"
                )

                st.write(
                    f"**Year:** {book['year']}"
                )

                if book["in_stock"]:

                    st.success(
                        "✅ In Stock"
                    )

                else:

                    st.error(
                        "❌ Out of Stock"
                    )

                if st.button(
                    "View Details",
                    key=f"view_{book['id']}",
                    use_container_width=True
                ):

                    st.session_state.selected_book = book
                    st.rerun()

                st.divider()