from libqtile import layout

from themes import Theme


class LayoutsCollection:

    def __init__(self, theme: Theme):
        layout_theme = {
            "border_width": 2,
            "margin": 8,
            "border_focus": theme.border_focus,
            "border_normal": theme.border_normal
        }

        self.column_layout = layout.Columns(
            border_on_single=True,
            border_normal_stack=theme.border_normal,
            border_focus_stack=theme.border_focus,
            **layout_theme
        )
        self.max_layout = layout.Max(**layout_theme)
        self.stack_layout = layout.Stack(num_stacks=2)
        self.bspwm_layout = layout.Bsp(**layout_theme)
        self.matrix_layout = layout.Matrix()
        self.monad_tall_layout = layout.MonadTall(
            change_ratio=0.2,
            **layout_theme
        )
        self.monad_wide_layout = layout.MonadWide(**layout_theme)
        self.ratio_tile_layout = layout.RatioTile(**layout_theme)
        self.tile_layout = layout.Tile(**layout_theme)
        self.tree_tab_layout = layout.TreeTab(
            panel_width=200,
            margin_y=10,
            active_bg=theme.active_border,
            inactive_bg=theme.border_normal,
            **layout_theme
        ),
        self.vertical_tile_layout = layout.VerticalTile(**layout_theme)
        self.zoomy_layout = layout.Zoomy(**layout_theme)
