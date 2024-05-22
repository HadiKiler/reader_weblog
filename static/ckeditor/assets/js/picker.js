const classicPicker = document.querySelectorAll('.picker-classic');
const classicContainer = document.querySelectorAll('.theme-classic');

const optionedPicker = document.querySelectorAll('.picker-optioned');
const optionedContainer = document.querySelectorAll('.theme-optioned');

const nanoPicker = document.querySelectorAll('.picker-nano');
const nanoContainer = document.querySelectorAll('.theme-nano');

// CLASSIC
try {
    // console.log(classicPicker, classicContainer)
    const themes = [
        [
            'classic',
            {
                swatches: [
                    'rgba(244, 67, 54, 1)',
                    'rgba(233, 30, 99, 0.95)',
                    'rgba(156, 39, 176, 0.9)',
                    'rgba(103, 58, 183, 0.85)',
                    'rgba(63, 81, 181, 0.8)',
                    'rgba(33, 150, 243, 0.75)',
                    'rgba(3, 169, 244, 0.7)',
                    'rgba(0, 188, 212, 0.7)',
                    'rgba(0, 150, 136, 0.75)',
                    'rgba(76, 175, 80, 0.8)',
                    'rgba(139, 195, 74, 0.85)',
                    'rgba(205, 220, 57, 0.9)',
                    'rgba(255, 235, 59, 0.95)',
                    'rgba(255, 193, 7, 1)'
                ],

                components: {
                    preview: true,
                    opacity: true,
                    hue: true,

                    interaction: {
                        hex: true,
                        rgba: true,
                        hsva: true,
                        input: true,
                        clear: true,
                        save: true
                    }
                }
            }
        ],
    ];
    for (let i = 0; i < classicContainer.length; i++) {
        const buttons = [];
        let pickr = null;

        for (const [theme, config] of themes) {
            const button = document.createElement('input');
            button.innerHTML = theme;
            buttons.push(button);

            button.addEventListener('click', () => {
                const el = document.createElement('p');
                classicPicker[i].appendChild(el);

                // Delete previous instance
                if (pickr) {
                    pickr.destroyAndRemove();
                }

                // Apply active class
                // for (const btn of buttons) {
                //     btn.classList[btn === button ? 'add' : 'remove']('active');
                // }

                // Create fresh instance
                pickr = new Pickr(Object.assign({
                    el,
                    theme,
                    default: '#6c5ffc'
                }, config));

                // Set events
                pickr.on('init', instance => {
                    console.log('Event: "init"', instance);
                }).on('hide', instance => {
                    console.log('Event: "hide"', instance);
                }).on('show', (color, instance) => {
                    console.log('Event: "show"', color, instance);
                }).on('save', (color, instance) => {
                    console.log('Event: "save"', color, instance);
                }).on('clear', instance => {
                    console.log('Event: "clear"', instance);
                }).on('change', (color, source, instance) => {
                    console.log('Event: "change"', color, source, instance);
                }).on('changestop', (source, instance) => {
                    console.log('Event: "changestop"', source, instance);
                }).on('cancel', instance => {
                    console.log('cancel', pickr.getColor().toRGBA().toString(0));
                }).on('swatchselect', (color, instance) => {
                    console.log('Event: "swatchselect"', color, instance);
                });
            });

            classicContainer[i].appendChild(button);
        }

        buttons[0].click();
    }
} catch (e) {
    console.log(e);
}

// MONOLITH
try {
    // console.log(optionedContainer, optionedPicker)
    const monolithThemes = [
        [
            'monolith',
            {
                swatches: [
                    'rgba(244, 67, 54, 1)',
                    'rgba(233, 30, 99, 0.95)',
                    'rgba(156, 39, 176, 0.9)',
                    'rgba(103, 58, 183, 0.85)',
                    'rgba(63, 81, 181, 0.8)',
                    'rgba(33, 150, 243, 0.75)',
                    'rgba(3, 169, 244, 0.7)'
                ],

                defaultRepresentation: 'HEXA',
                components: {
                    preview: true,
                    opacity: true,
                    hue: true,

                    interaction: {
                        hex: false,
                        rgba: true,
                        hsva: false,
                        input: true,
                        clear: true,
                        save: true
                    }
                }
            }
        ]
    ];
    for (let i = 0; i < optionedContainer.length; i++) {
        let inputColor = $(`#${optionedPicker[i].id.toString()}`);
        let color = '';
        const monolithButtons = [];
        let monolithPickr = null;

        for (const [theme, config] of monolithThemes) {
            const inp = document.createElement('input');
            inp.setAttribute('hidden', 'hidden');
            inp.innerHTML = theme;
            monolithButtons.push(inp);

            inp.addEventListener('click', () => {
                const el = document.createElement('p');
                optionedPicker[i].appendChild(el);

                // Delete previous instance
                if (monolithPickr) {
                    monolithPickr.destroyAndRemove();
                }

                // Apply active class
                for (const btn of monolithButtons) {
                    btn.classList[btn === inp ? 'add' : 'remove']('active');
                }

                // Create fresh instance
                monolithPickr = new Pickr(Object.assign({
                    el,
                    theme,
                    default: 'rgba(102,255,0,0.92)'
                }, config));


                // Set events
                monolithPickr.on('init', () => {
                    inputColor.val(monolithPickr.getColor().toHEXA().toString());
                    inputColor.attr('value', monolithPickr.getColor().toHEXA().toString());
                    inputColor.css('color', inputColor.val());
                }).on('hide', () => {
                    inputColor.val(monolithPickr.getColor().toHEXA().toString());
                    inputColor.attr('value', monolithPickr.getColor().toHEXA().toString());
                    inputColor.css('color', inputColor.val());
                }).on('show', () => {
                    inputColor.val(monolithPickr.getColor().toHEXA().toString());
                    inputColor.attr('value', monolithPickr.getColor().toHEXA().toString());
                    inputColor.css('color', inputColor.val());
                }).on('save', () => {
                    inputColor.val(monolithPickr.getColor().toHEXA().toString());
                    inputColor.attr('value', monolithPickr.getColor().toHEXA().toString());
                    inputColor.css('color', inputColor.val());
                }).on('clear', () => {
                    inputColor.val(monolithPickr.getColor().toHEXA().toString());
                    inputColor.attr('value', monolithPickr.getColor().toHEXA().toString());
                    inputColor.css('color', inputColor.val());
                }).on('change', () => {
                    inputColor.val(monolithPickr.getColor().toHEXA().toString());
                    inputColor.attr('value', monolithPickr.getColor().toHEXA().toString());
                    inputColor.css('color', inputColor.val());
                }).on('changestop', () => {
                    inputColor.val(monolithPickr.getColor().toHEXA().toString());
                    inputColor.attr('value', monolithPickr.getColor().toHEXA().toString());
                    inputColor.css('color', inputColor.val());
                }).on('cancel', () => {
                    inputColor.val(monolithPickr.getColor().toHEXA().toString());
                    inputColor.attr('value', monolithPickr.getColor().toHEXA().toString());
                    inputColor.css('color', inputColor.val());
                }).on('swatchselect', () => {
                    inputColor.val(monolithPickr.getColor().toHEXA().toString());
                    inputColor.attr('value', monolithPickr.getColor().toHEXA().toString());
                    inputColor.css('color', inputColor.val());
                });
            });
            optionedContainer[i].appendChild(inp);
        }
        monolithButtons[0].click();
    }
} catch (e) {
    console.log(e);
}


// NANO
try {
    // console.log(nanoContainer, nanoPicker);
    const nanoThemes = [
        [
            'nano',
            {
                swatches: [
                    'rgba(244, 67, 54, 1)',
                    'rgba(233, 30, 99, 0.95)',
                    'rgba(156, 39, 176, 0.9)',
                    'rgba(103, 58, 183, 0.85)',
                    'rgba(63, 81, 181, 0.8)',
                    'rgba(33, 150, 243, 0.75)',
                    'rgba(3, 169, 244, 0.7)'
                ],

                defaultRepresentation: 'HEXA',
                components: {
                    preview: true,
                    opacity: true,
                    hue: true,

                    interaction: {
                        hex: false,
                        rgba: false,
                        hsva: false,
                        input: true,
                        clear: true,
                        save: true
                    }
                }
            }
        ]
    ];
    for (let i = 0; i < nanoContainer.length; i++) {
        const nanoButtons = [];
        let nanoPickr = null;

        for (const [theme, config] of nanoThemes) {
            const button = document.createElement('input');
            button.innerHTML = theme;
            nanoButtons.push(button);

            button.addEventListener('click', () => {
                const el = document.createElement('p');
                nanoPicker[i].appendChild(el);

                // Delete previous instance
                if (nanoPickr) {
                    nanoPickr.destroyAndRemove();
                }

                // Apply active class
                // for (const btn of nanoButtons) {
                //     btn.classList[btn === button ? 'add' : 'remove']('active');
                // }

                // Create fresh instance
                nanoPickr = new Pickr(Object.assign({
                    el,
                    theme,
                    default: 'rgba(255,0,0,1)'
                }, config));

                // Set events
                nanoPickr.on('init', instance => {
                    console.log('Event: "init"', instance);
                }).on('hide', instance => {
                    console.log('Event: "hide"', instance);
                }).on('show', (color, instance) => {
                    console.log('Event: "show"', color, instance);
                }).on('save', (color, instance) => {
                    console.log('Event: "save"', color, instance);
                }).on('clear', instance => {
                    console.log('Event: "clear"', instance);
                }).on('change', (color, source, instance) => {
                    console.log('Event: "change"', color, source, instance);
                }).on('changestop', (source, instance) => {
                    console.log('Event: "changestop"', source, instance);
                }).on('cancel', instance => {
                    console.log('cancel', nanoPickr.getColor().toRGBA().toString(0));
                }).on('swatchselect', (color, instance) => {
                    console.log('Event: "swatchselect"', color, instance);
                });


            });

            // nanoContainer[i].appendChild(button);
        }
        nanoButtons[0].click();
    }
} catch (e) {
    console.log(e);
}
