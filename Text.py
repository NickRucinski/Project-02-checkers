import pygame


class Text:
    def __init__(self, text: str, screen: pygame.display, position, font, color, render_function=None, max_size=1000):
        self.maxSize = max_size
        self.text = text
        self.screen = screen
        self.position = position
        self.color = color
        self.font = font
        self.render_function = render_function or self.render  # Default to render if render_function is not provided
        self.line_height = 0

        self.render_function()

    def render(self):
        text = self.font.render(
            self.text,
            True,
            self.color
        )
        rect = text.get_rect(center=self.position)
        self.screen.blit(text, rect)
        self.line_height = text.get_height()

    def render_with_wrapping(self) -> int:
        """
        Renders text to a max width in pixel and wraps the text at that point
        """
        words = self.text.split(' ')
        lines = []
        current_line = ''

        for word in words:
            test_line = current_line + ' ' + word if current_line else word
            text_surface = self.font.render(test_line, True, self.color)
            if text_surface.get_width() <= self.maxSize or '\n' in word:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        y = self.position[1]
        for line in lines:
            text_surface = self.font.render(line, True, self.color)
            self.screen.blit(text_surface, (self.position[0], y))
            y += text_surface.get_height()
        return y
