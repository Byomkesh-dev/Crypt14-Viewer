document.addEventListener('DOMContentLoaded', () => {
    // Basic hash router
    function handleHashChange() {
        const hash = window.location.hash.slice(1);
        document.querySelectorAll('.chat').forEach(chat => chat.classList.remove('active'));
        if (hash) {
            const el = document.querySelector('.chat[data-chatid="' + hash + '"]');
            if (el) el.classList.add('active');
        }
    }
    window.addEventListener('hashchange', handleHashChange);
    handleHashChange(); // Trigger on initial load
    
    // Auto-scroll logic if a chat is opened
    function scrollDown() {
        const content = document.getElementById('content');
        if(content) content.scrollTop = content.scrollHeight;
    }
    
    document.querySelectorAll('.chat-partner a').forEach(a => {
        a.addEventListener('click', () => {
             setTimeout(scrollDown, 10);
        });
    });
});
